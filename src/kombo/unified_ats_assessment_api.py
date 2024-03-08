"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from kombo import utils
from kombo._hooks import HookContext
from kombo.models import errors, operations, shared
from typing import Optional

class UnifiedATSAssessmentAPI:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def get_assessment_orders_open(self, x_integration_id: str, cursor: Optional[str] = None, page_size: Optional[int] = None) -> operations.GetAssessmentOrdersOpenResponse:
        r"""Get open orders
        Get all open assessment orders of an integration.
        """
        hook_ctx = HookContext(operation_id='GetAssessmentOrdersOpen', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetAssessmentOrdersOpenRequest(
            x_integration_id=x_integration_id,
            cursor=cursor,
            page_size=page_size,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/assessment/orders/open'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        query_params = { **utils.get_query_params(operations.GetAssessmentOrdersOpenRequest, request), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.GetAssessmentOrdersOpenResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetAssessmentOrdersOpenSuccessfulResponse])
                res.get_assessment_orders_open_successful_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.GetAssessmentOrdersOpenErrorResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_assessment_packages(self, x_integration_id: str) -> operations.GetAssessmentPackagesResponse:
        r"""Get packages
        Get all available assessment packages for an integration.

        This is mainly intended for debugging. As you always need to submit the full list of available packages when using [\"set packages\"](/assessment/v1/put-packages), there shouldn't ever be a need to call this endpoint in production.
        """
        hook_ctx = HookContext(operation_id='GetAssessmentPackages', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetAssessmentPackagesRequest(
            x_integration_id=x_integration_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/assessment/packages'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('GET', url, params=query_params, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.GetAssessmentPackagesResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.GetAssessmentPackagesSuccessfulResponse])
                res.get_assessment_packages_successful_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.GetAssessmentPackagesErrorResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def put_assessment_orders_assessment_order_id_result(self, x_integration_id: str, assessment_order_id: str, request_body: Optional[operations.PutAssessmentOrdersAssessmentOrderIDResultRequestBody] = None) -> operations.PutAssessmentOrdersAssessmentOrderIDResultResponse:
        r"""Update order result
        Updates an assessment order result.

        <Accordion title=\"Supported integrations\" icon=\"list-check\">
        This feature is currently available for the following integrations:

        <ul>
        <li style={{display: 'flex', alignItems: 'center'}}><img
          src=\"https://storage.googleapis.com/kombo-assets/integrations/workday/icon.svg\"
          style={{\"width\":\"16px\",\"height\":\"16px\",\"marginTop\":\"0 !important\",\"marginBottom\":\"0 !important\",\"marginRight\":\"8px !important\"}}
        />Workday</li>
        <li style={{display: 'flex', alignItems: 'center'}}><img
          src=\"https://storage.googleapis.com/kombo-assets/integrations/successfactors/icon.svg\"
          style={{\"width\":\"16px\",\"height\":\"16px\",\"marginTop\":\"0 !important\",\"marginBottom\":\"0 !important\",\"marginRight\":\"8px !important\"}}
        />SAP SuccessFactors</li>
        <li style={{display: 'flex', alignItems: 'center'}}><img
          src=\"https://storage.googleapis.com/kombo-assets/integrations/smartrecruiters/icon.svg\"
          style={{\"width\":\"16px\",\"height\":\"16px\",\"marginTop\":\"0 !important\",\"marginBottom\":\"0 !important\",\"marginRight\":\"8px !important\"}}
        />SmartRecruiters</li>
        <li style={{display: 'flex', alignItems: 'center'}}><img
          src=\"https://storage.googleapis.com/kombo-assets/integrations/recruitee/icon.svg\"
          style={{\"width\":\"16px\",\"height\":\"16px\",\"marginTop\":\"0 !important\",\"marginBottom\":\"0 !important\",\"marginRight\":\"8px !important\"}}
        />Recruitee</li>
        <li style={{display: 'flex', alignItems: 'center'}}><img
          src=\"https://storage.googleapis.com/kombo-assets/integrations/greenhouse/icon.svg\"
          style={{\"width\":\"16px\",\"height\":\"16px\",\"marginTop\":\"0 !important\",\"marginBottom\":\"0 !important\",\"marginRight\":\"8px !important\"}}
        />Greenhouse</li>
        <li style={{display: 'flex', alignItems: 'center'}}><img
          src=\"https://storage.googleapis.com/kombo-assets/integrations/ashby/icon.svg\"
          style={{\"width\":\"16px\",\"height\":\"16px\",\"marginTop\":\"0 !important\",\"marginBottom\":\"0 !important\",\"marginRight\":\"8px !important\"}}
        />Ashby</li>
        </ul>

        You'd like to see this feature for another integration? Please reach out!
        We're always happy to discuss extending our coverage.
        </Accordion>
        ### Example Request Body

        ```json
        {
          \"status\": \"COMPLETED\",
          \"result_url\": \"https://example.com\",
          \"completed_at\": \"2023-04-04T00:00:00.000Z\",
          \"score\": 90,
          \"max_score\": 100,
          \"attributes\": [
            {
              \"field\": \"remarks\",
              \"value\": \"Test completed with passing score\"
            }
          ]
        }
        ```
        """
        hook_ctx = HookContext(operation_id='PutAssessmentOrdersAssessmentOrderIdResult', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.PutAssessmentOrdersAssessmentOrderIDResultRequest(
            x_integration_id=x_integration_id,
            assessment_order_id=assessment_order_id,
            request_body=request_body,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutAssessmentOrdersAssessmentOrderIDResultRequest, base_url, '/assessment/orders/{assessment_order_id}/result', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.PutAssessmentOrdersAssessmentOrderIDResultRequest, "request_body", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('PUT', url, params=query_params, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','401','403','404','4XX','503','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.PutAssessmentOrdersAssessmentOrderIDResultResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.PutAssessmentOrdersAssessmentOrderIDResultSuccessfulResponse])
                res.put_assessment_orders_assessment_order_id_result_successful_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.PutAssessmentOrdersAssessmentOrderIDResultErrorResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.PutAssessmentOrdersAssessmentOrderIDResultResponseBody)
                out.raw_response = http_res
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 403:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseBody)
                out.raw_response = http_res
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 404:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponseResponseBody)
                out.raw_response = http_res
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 503:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.PutAssessmentOrdersAssessmentOrderIDResultUnifiedATSAssessmentAPIResponse503ResponseBody)
                out.raw_response = http_res
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def put_assessment_packages(self, x_integration_id: str, request_body: Optional[operations.PutAssessmentPackagesRequestBody] = None) -> operations.PutAssessmentPackagesResponse:
        r"""Set packages
        Replaces the list of available assessment packages.

        Packages that have been previously submitted through this endpoint but aren't included again will be marked as deleted.
        """
        hook_ctx = HookContext(operation_id='PutAssessmentPackages', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.PutAssessmentPackagesRequest(
            x_integration_id=x_integration_id,
            request_body=request_body,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/assessment/packages'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.PutAssessmentPackagesRequest, "request_body", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('PUT', url, params=query_params, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        
        res = operations.PutAssessmentPackagesResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type'), raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[shared.PutAssessmentPackagesSuccessfulResponse])
                res.put_assessment_packages_successful_response = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(http_res.headers.get('Content-Type'), 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.PutAssessmentPackagesErrorResponse)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    