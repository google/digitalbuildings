package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ICooling;
import www.google.com.digitalbuildings._0_0_1.subfields.Cooling;
import www.google.com.digitalbuildings._0_0_1.subfields.IRequest;
import www.google.com.digitalbuildings._0_0_1.subfields.Request;
import www.google.com.digitalbuildings._0_0_1.subfields.ICount;
import www.google.com.digitalbuildings._0_0_1.subfields.Count;


@SuppressWarnings("serial")
public class Cooling_request_count extends www.google.com.digitalbuildings._0_0_1.fields.Field implements ICooling_request_count{

	IRI newInstance;
	public Cooling_request_count(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Cooling_request_count"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfCooling (ICooling parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICooling> getComposedOfCooling (){
		Set<ICooling> ComposedOfCooling = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling) {
				ComposedOfCooling.add((Cooling)action);
			}
		});
		return ComposedOfCooling;
	}


  public void addComposedOfCount (ICount parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICount> getComposedOfCount (){
		Set<ICount> ComposedOfCount = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Count) {
				ComposedOfCount.add((Count)action);
			}
		});
		return ComposedOfCount;
	}


  public void addComposedOfRequest (IRequest parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IRequest> getComposedOfRequest (){
		Set<IRequest> ComposedOfRequest = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Request) {
				ComposedOfRequest.add((Request)action);
			}
		});
		return ComposedOfRequest;
	}

	public static Set<ICooling_request_count> getAllCooling_request_countsObjectsCreated(){
		Set<ICooling_request_count> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Cooling_request_count")).subjects().stream()
		.map(mapper->(ICooling_request_count)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}