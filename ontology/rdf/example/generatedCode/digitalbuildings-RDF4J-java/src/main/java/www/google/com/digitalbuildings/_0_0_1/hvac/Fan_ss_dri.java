package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.facilities.IPhysicalLocation;
import www.google.com.digitalbuildings._0_0_1.facilities.PhysicalLocation;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status;

/**
* Class Fan_ss_dri 
* Dryer-interlocked fan.
*/
@SuppressWarnings("serial")
public class Fan_ss_dri extends www.google.com.digitalbuildings._0_0_1.hvac.Ss implements IFan_ss_dri{

	IRI newInstance;
	public Fan_ss_dri(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_dri"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDryer_run_status (IDryer_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status> getUsesDryer_run_status (){
		Set<IDryer_run_status> UsesDryer_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status) {
				UsesDryer_run_status.add((Dryer_run_status)action);
			}
		});
		return UsesDryer_run_status;
	}


  public void addPhysicalLocation (IPhysicalLocation parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasPhysicalLocation"), parameter);
	}

	public Set<IPhysicalLocation> getPhysicalLocation(){
		Set<IPhysicalLocation> physicalLocations = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasPhysicalLocation"), null)
		.objects().forEach(action->{
			if(action instanceof PhysicalLocation) {
				physicalLocations.add((PhysicalLocation)action);
			}
		});
		return physicalLocations;
	}

	public static Set<IFan_ss_dri> getAllFan_ss_drisObjectsCreated(){
		Set<IFan_ss_dri> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_dri")).subjects().stream()
		.map(mapper->(IFan_ss_dri)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}